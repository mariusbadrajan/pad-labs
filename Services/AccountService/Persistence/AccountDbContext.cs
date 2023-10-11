using AccountService.Entities;
using Microsoft.EntityFrameworkCore;

namespace AccountService.Persistence;

public class AccountDbContext : DbContext
{
    private readonly IConfiguration _configuration;

    public AccountDbContext(IConfiguration configuration)
    {
        _configuration = configuration;
    }
    protected override void OnConfiguring(DbContextOptionsBuilder options)
    {
        options.UseSqlServer(_configuration.GetConnectionString("AccountDbConnection"));
    }

    public DbSet<UserAccount> UserAccounts { get; set; }
}