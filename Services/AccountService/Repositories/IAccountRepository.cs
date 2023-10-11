using AccountService.Entities;

namespace AccountService.Repositories;

public interface IAccountRepository
{
    public Task<List<UserAccount>> GetAllUserAccountsAsync();
    public Task<List<UserAccount>> GetAllAccountsByUserIdAsync(Guid userId);
    public Task<UserAccount> GetUserAccountByIdAsync(Guid id);
    public Task<UserAccount> AddUserAccountAsync(UserAccount account);
    public Task<UserAccount> UpdateUserAccountAsync(UserAccount account);
    public Task DeleteUserAccountByIdAsync(Guid id);
}