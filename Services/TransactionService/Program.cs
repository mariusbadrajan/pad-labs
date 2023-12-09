using AccountService.Services;
using Microsoft.AspNetCore.Http.Timeouts;
using TransactionService.Interceptors;
using TransactionService.Persistence;
using TransactionService.Repositories;

var builder = WebApplication.CreateBuilder(args);

// Additional configuration is required to successfully run gRPC on macOS.
// For instructions on how to configure Kestrel and gRPC clients on macOS, visit https://go.microsoft.com/fwlink/?linkid=2099682

// Add services to the container.
builder.Services.AddGrpc(options => { options.Interceptors.Add<RequestInterceptor>(); });
builder.Services.AddScoped<IRepository, Repository>();
builder.Services.AddDbContext<TransactionDbContext>();
builder.Services.AddAutoMapper(typeof(Program));
// Will work only with REST request and not GRPC ones
builder.Services.AddRequestTimeouts(options =>
{
    options.DefaultPolicy =
        new RequestTimeoutPolicy
        {
            Timeout = TimeSpan.FromSeconds(2),
            TimeoutStatusCode = 503
        };
});

var app = builder.Build();

// Configure the HTTP request pipeline.
app.UseRequestTimeouts();
app.MapGrpcService<TransactionService.Services.TransactionService>();
app.MapGrpcService<ManagerService>();
app.MapGet("/",
    () =>
        "Communication with gRPC endpoints must be made through a gRPC client. To learn how to create a client, visit: https://go.microsoft.com/fwlink/?linkid=2086909");

ManagerService.RegisterService();

app.Run();