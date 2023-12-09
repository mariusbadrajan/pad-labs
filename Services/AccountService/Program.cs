using AccountService.Interceptors;
using AccountService.Persistence;
using AccountService.Repositories;
using AccountService.Services;

var builder = WebApplication.CreateBuilder(args);

// Additional configuration is required to successfully run gRPC on macOS.
// For instructions on how to configure Kestrel and gRPC clients on macOS, visit https://go.microsoft.com/fwlink/?linkid=2099682

// Add services to the container.
builder.Services.AddGrpc(options => { options.Interceptors.Add<RequestInterceptor>(); });
builder.Services.AddScoped<IRepository, Repository>();
builder.Services.AddDbContext<AccountDbContext>();
builder.Services.AddAutoMapper(typeof(Program));

var app = builder.Build();

// Configure the HTTP request pipeline.
app.MapGrpcService<AccountService.Services.AccountService>();
app.MapGrpcService<ManagerService>();
//app.MapGrpcService<AccountService.Services.Manager>();
app.MapGet("/",
    () =>
        "Communication with gRPC endpoints must be made through a gRPC client. To learn how to create a client, visit: https://go.microsoft.com/fwlink/?linkid=2086909");

ManagerService.RegisterService();

app.Run();