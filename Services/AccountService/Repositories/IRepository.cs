using AccountService.Entities;

namespace AccountService.Repositories;

public interface IRepository
{
    public Task<List<Account>> GetAllUserAccountsAsync(int userId);
    public Task<Account> GetAccountByIdAsync(int id);
    public Task<Account> AddAccountAsync(Account account);
    public Task<Account> UpdateAccountAsync(Account account);
    public Task DeleteAccountByIdAsync(int id);
}