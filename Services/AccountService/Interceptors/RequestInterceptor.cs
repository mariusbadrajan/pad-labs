using Grpc.Core;
using Grpc.Core.Interceptors;

namespace AccountService.Interceptors
{
    public class RequestInterceptor : Interceptor
    {
        private readonly ILogger _logger;

        private const int _maxTransactionTimeoutMs = 5000;

        public RequestInterceptor(ILogger<RequestInterceptor> logger)
        {
            _logger = logger;
        }

        public override async Task<TResponse> UnaryServerHandler<TRequest, TResponse>(
        TRequest request,
        ServerCallContext context,
        UnaryServerMethod<TRequest, TResponse> continuation)
        {
            _logger.LogInformation("Starting receiving call. Type/Method: {Type} / {Method}.",
                MethodType.Unary, context.Method);

            var cancellationTokenSource = new CancellationTokenSource();
            var timeoutTask = Task.Delay(TimeSpan.FromMilliseconds(_maxTransactionTimeoutMs), cancellationTokenSource.Token);

            try
            {
                var actualTask = continuation(request, context);
                var completedTask = await Task.WhenAny(actualTask, timeoutTask);

                if (completedTask == timeoutTask)
                {
                    cancellationTokenSource.Cancel();
                    _logger.LogWarning($"Call timed out for method: {context.Method}.");
                    throw new RpcException(new Status(StatusCode.DeadlineExceeded, "Call timed out"));
                }

                return await actualTask;
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, $"Error thrown by {context.Method}.");
                throw;
            }
        }
    }
}
