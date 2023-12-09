using AccountService.Entities;
using AccountService.Persistence;
using Microsoft.EntityFrameworkCore;

namespace AccountService.Repositories;

public class Repository : IRepository
{
    private readonly AccountDbContext _dbContext;

    public Repository(AccountDbContext dbContext)
    {
        _dbContext = dbContext;
    }

    public async Task<List<Account>> GetAllUserAccountsAsync(int userId)
    {
        return await _dbContext.Accounts.Where(x => x.UserId == userId).ToListAsync();
    }

    public async Task<Account?> GetAccountByIdAsync(int id)
    {
        return await _dbContext.Accounts.AsNoTracking().FirstOrDefaultAsync(x => x.Id == id);
    }

    public async Task<Account> AddAccountAsync(Account account)
    {
        var result = _dbContext.Accounts.Add(account);
        await _dbContext.SaveChangesAsync();
        return result.Entity;
    }

    public async Task<Account> UpdateAccountAsync(Account account)
    {
        var result = _dbContext.Accounts.Update(account);
        await _dbContext.SaveChangesAsync();
        return result.Entity;
    }

    public async Task DeleteAccountByIdAsync(Account account)
    {
        _dbContext.Remove(account);
        await _dbContext.SaveChangesAsync();
    }
}