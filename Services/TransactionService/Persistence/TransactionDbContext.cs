using Microsoft.EntityFrameworkCore;
using TransactionService.Entities;

namespace TransactionService.Persistence;

public class TransactionDbContext : DbContext
{
    private readonly IConfiguration _configuration;

    public TransactionDbContext(IConfiguration configuration)
    {
        _configuration = configuration;
    }
    protected override void OnConfiguring(DbContextOptionsBuilder options)
    {
        options.UseSqlServer(_configuration.GetConnectionString("TransactionDbConnection"));
    }

    public DbSet<Transaction> Transactions { get; set; }
}