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

    public async Task<Transaction> GetTransactionByIdAsync(int id)
    {
        return await _dbContext.Transactions.AsNoTracking().FirstOrDefaultAsync(x => x.Id == id);
    }

    public async Task<Transaction> AddTransactionAsync(Transaction account)
    {
        var result = _dbContext.Transactions.Add(account);
        await _dbContext.SaveChangesAsync();
        return result.Entity;
    }

    public async Task<Transaction> UpdateTransactionAsync(Transaction account)
    {
        var result = _dbContext.Transactions.Update(account);
        await _dbContext.SaveChangesAsync();
        return result.Entity;
    }

    public async Task DeleteTransactionByIdAsync(int id)
    {
        var userAccount = await _dbContext.Transactions.FirstOrDefaultAsync(x => x.Id == id);
        _dbContext.Remove(userAccount);
        await _dbContext.SaveChangesAsync();
    }
}