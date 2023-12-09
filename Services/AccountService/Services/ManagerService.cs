using Grpc.Core;
using Grpc.Net.Client;
using Microsoft.Data.SqlClient;
using Protos.Manager;
using System.Text.RegularExpressions;

namespace AccountService.Services;

public class ManagerService : Protos.Manager.ManagerService.ManagerServiceBase
{
    private const string appUrlsKey = "ASPNETCORE_URLS";
    private const int maxRegisterRetries = 3;
    private const int registerRetryDelayMs = 3000;

    public ManagerService()
    {

    }

    public override async Task<GetHealthStatusResponse> GetHealthStatus(GetHealthStatusRequest request, ServerCallContext context)
    {
        using var connection = new SqlConnection("Server=MDMOB40630; Database=TransactionsDb; Integrated Security=True; TrustServerCertificate=True;");

        await connection.OpenAsync();
        if (connection.State != System.Data.ConnectionState.Open)
        {
            // implement restart server logic
            context.Status = new Status(StatusCode.Unavailable, "");
            return new GetHealthStatusResponse { HealthStatus = HealthStatus.Down };
        }

        return new GetHealthStatusResponse { HealthStatus = HealthStatus.Up };
    }

    public static async void RegisterService()
    {
        var connected = false;
        var retries = 0;

        var serviceDiscoveryHost = "http://localhost:50051";
        var hostName = Environment.GetEnvironmentVariable(appUrlsKey)!
                                  .Split(';')
                                  .FirstOrDefault(x => Regex.IsMatch(x, @"^http://"))!;

        using var channel = GrpcChannel.ForAddress(serviceDiscoveryHost);
        var client = new Protos.Manager.ManagerService.ManagerServiceClient(channel);
        var registerServiceRequest =
            new RegisterServiceRequest
            {
                ServiceType = ServiceType.Account,
                Host = hostName
            };

        while (!connected && retries < maxRegisterRetries)
        {
            try
            {
                await client.RegisterServiceAsync(registerServiceRequest);
                Console.WriteLine($"{registerServiceRequest.ServiceType} service was successfully registered to {serviceDiscoveryHost}.");
                connected = true;
            }
            catch (RpcException ex)
            {
                Console.WriteLine($"Failed to register {registerServiceRequest.ServiceType} service to {serviceDiscoveryHost}: {ex.Status.StatusCode}, Retry: {retries + 1}");

                retries++;
                await Task.Delay(registerRetryDelayMs);
            }
        }

        if (!connected)
        {
            Console.WriteLine("Failed to register service after all retries.");
        }
    }
}
