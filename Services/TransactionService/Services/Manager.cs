using Grpc.Core;
using Microsoft.Data.SqlClient;
using TransactionService.Proto;
using ManagerService = TransactionService.Proto.ManagerService;


namespace AccountService.Services
{
    public class Manager : ManagerService.ManagerServiceBase
    {
        public override async Task<Response> GetHealthStatus(Request request, ServerCallContext context)
        {
            using var connection = new SqlConnection("Server=MDMOB40630; Database=AccountsDb; Integrated Security=True; TrustServerCertificate=True;");

            await connection.OpenAsync();
            if (connection.State != System.Data.ConnectionState.Open)
            {
                return new Response { HealthStatus = "Unhealthy" };
            }

            return new Response { HealthStatus = "Healthy" };
        }
    }
}
