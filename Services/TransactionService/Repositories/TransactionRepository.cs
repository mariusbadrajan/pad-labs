using Microsoft.EntityFrameworkCore;
using TransactionService.Entities;
using TransactionService.Persistence;

namespace TransactionService.Repositories;

public class TransactionRepository : ITransactionRepository
{
    private readonly TransactionDbContext _dbContext;

    public TransactionRepository(TransactionDbContext dbContext)
    {
        _dbContext = dbContext;
    }

    public async Task<List<Transaction>> GetAllTransactionsAsync()
    {
        return await _dbContext.Transactions.ToListAsync();
    }

    public async Task<List<Transaction>> GetAllTransactionsByUserIdAsync(Guid userId)
    {
        return await _dbContext.Transactions.Where(x => x.UserId == userId).ToListAsync();
    }

    public async Task<Transaction> GetTransactionByIdAsync(Guid id)
    {
        return await _dbContext.Transactions.FindAsync(id);
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

    public async Task DeleteTransactionByIdAsync(Guid id)
    {
        var userAccount = await _dbContext.Transactions.FirstOrDefaultAsync(x => x.Id == id);
        _dbContext.Remove(userAccount);
        await _dbContext.SaveChangesAsync();
    }
}