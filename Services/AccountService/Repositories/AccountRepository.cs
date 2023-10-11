using AccountService.Entities;
using AccountService.Persistence;
using Microsoft.EntityFrameworkCore;

namespace AccountService.Repositories;

public class AccountRepository : IAccountRepository
{
    private readonly AccountDbContext _dbContext;

    public AccountRepository(AccountDbContext dbContext)
    {
        _dbContext = dbContext;
    }

    public async Task<List<UserAccount>> GetAllUserAccountsAsync()
    {
        return await _dbContext.UserAccounts.ToListAsync();
    }

    public async Task<List<UserAccount>> GetAllAccountsByUserIdAsync(Guid userId)
    {
        return await _dbContext.UserAccounts.Where(x => x.UserId == userId).ToListAsync();
    }

    public async Task<UserAccount> GetUserAccountByIdAsync(Guid id)
    {
        return await _dbContext.UserAccounts.FindAsync(id);
    }

    public async Task<UserAccount> AddUserAccountAsync(UserAccount account)
    {
        var result = _dbContext.UserAccounts.Add(account);
        await _dbContext.SaveChangesAsync();
        return result.Entity;
    }

    public async Task<UserAccount> UpdateUserAccountAsync(UserAccount account)
    {
        var result = _dbContext.UserAccounts.Update(account);
        await _dbContext.SaveChangesAsync();
        return result.Entity;
    }

    public async Task DeleteUserAccountByIdAsync(Guid id)
    {
        var userAccount = await _dbContext.UserAccounts.FirstOrDefaultAsync(x => x.Id == id);
        _dbContext.Remove(userAccount);
        await _dbContext.SaveChangesAsync();
    }
}