using Grpc.Core;
using Grpc.Core.Interceptors;

namespace TransactionService.Interceptors
{
    public class RequestInterceptor : Interceptor
    {
        private readonly ILogger _logger;
        private readonly int _maxTransactionAmount = 100;

        public RequestInterceptor(ILogger<RequestInterceptor> logger)
        {
            _logger = logger;
        }

        public override async Task<TResponse> UnaryServerHandler<TRequest, TResponse>(
        TRequest request,
        ServerCallContext context,
        UnaryServerMethod<TRequest, TResponse> continuation)
        {
            _logger.LogInformation("Starting receiving call. Type/Method: {Type} / {Method}",
                MethodType.Unary, context.Method);
            try
            {
                var test = continuation(request, context);

                return test.Result;
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, $"Error thrown by {context.Method}.");
                throw;
            }
        }
    }
}
