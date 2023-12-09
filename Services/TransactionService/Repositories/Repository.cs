using Microsoft.EntityFrameworkCore;
using TransactionService.Entities;
using TransactionService.Persistence;

namespace TransactionService.Repositories;

public class Repository : IRepository
{
    private readonly TransactionDbContext _dbContext;

    public Repository(TransactionDbContext dbContext)
    {
        _dbContext = dbContext;
    }

    public async Task<List<Transaction>> GetAllUserTransactionsAsync(int userId)
    {
        return await _dbContext.Transactions.Where(x => x.UserId == userId).ToListAsync();
    }

    public async Task<List<Transaction>> GetAllAccountTransactionsAsync(int accountId)
    {
        return await _dbContext.Transactions.Where(x => x.AccountId == accountId).ToListAsync();
    }

    public async Task<Transaction?> GetTransactionByIdAsync(int id)
    {
        return await _dbContext.Transactions.AsNoTracking().FirstOrDefaultAsync(x => x.Id == id);
    }

    public async Task<Transaction> AddTransactionAsync(Transaction transaction)
    {
        var result = _dbContext.Transactions.Add(transaction);
        await _dbContext.SaveChangesAsync();
        return result.Entity;
    }

    public async Task<Transaction> UpdateTransactionAsync(Transaction transaction)
    {
        var result = _dbContext.Transactions.Update(transaction);
        await _dbContext.SaveChangesAsync();
        return result.Entity;
    }

    public async Task DeleteTransactionByIdAsync(Transaction transaction)
    {
        _dbContext.Remove(transaction);
        await _dbContext.SaveChangesAsync();
    }
}