using AccountService.Proto;
using AccountService.Repositories;
using Grpc.Core;
using AccountServices = AccountService.Proto.AccountService;

namespace AccountService.Services;

public class AccountService : AccountServices.AccountServiceBase
{
    private readonly IAccountRepository _accountRepository;

    public AccountService(IAccountRepository accountRepository)
    {
        _accountRepository = accountRepository;
    }
    
    public override async Task<UserAccounts> GetUserAccounts(Empty request, ServerCallContext context)
    {
        var dbUserAccounts = await _accountRepository.GetAllUserAccountsAsync();
        
        var userAccounts = new UserAccounts();
        foreach (var userAccount in dbUserAccounts)
        {
            userAccounts.Accounts.Add(new UserAccount
            {
                Id = userAccount.Id.ToString("D"),
                UserId = userAccount.UserId.ToString("D"),
                Balance = userAccount.Balance
            });
        }

        return userAccounts;
    }

    public override async Task<UserAccounts> GetAccountsByUserId(GetAccountsByUserIdRequest request,
        ServerCallContext context)
    {
        var dbUserAccounts = await _accountRepository.GetAllAccountsByUserIdAsync(new Guid(request.UserId));
        
        var userAccounts = new UserAccounts();
        foreach (var userAccount in dbUserAccounts)
        {
            userAccounts.Accounts.Add(new UserAccount
            {
                Id = userAccount.Id.ToString("D"),
                UserId = userAccount.UserId.ToString("D"),
                Balance = userAccount.Balance
            });
        }

        return userAccounts;
    }

    public override async Task<UserAccount> GetUserAccountById(GetUserAccountByIdRequest request,
        ServerCallContext context)
    {
        var dbUserAccount = await _accountRepository.GetUserAccountByIdAsync(new Guid(request.Id));

        var userAccount = new UserAccount
        {
            Id = dbUserAccount.Id.ToString("D"),
            UserId = dbUserAccount.UserId.ToString("D"),
            Balance = dbUserAccount.Balance
        };

        return userAccount;
    }

    public override async Task<UserAccount> AddUserAccount(AddUserAccountRequest request,
        ServerCallContext context)
    {
        var dbUserAccount = new Entities.UserAccount
        {
            Id = new Guid(request.Account.Id),
            UserId = new Guid(request.Account.UserId),
            Balance = request.Account.Balance
        };

        var userAccount = await _accountRepository.AddUserAccountAsync(dbUserAccount);

        return request.Account;
    }

    public override async Task<UserAccount> UpdateOffer(UpdateUserAccountRequest request,
        ServerCallContext context)
    {
        var dbUserAccount = new Entities.UserAccount
        {
            Id = new Guid(request.Account.Id),
            UserId = new Guid(request.Account.UserId),
            Balance = request.Account.Balance
        };

        var userAccount = await _accountRepository.UpdateUserAccountAsync(dbUserAccount);

        return request.Account;
    }
    
    public override async Task<Empty> DeleteOffer(DeleteUserAccountRequest request,
        ServerCallContext context)
    {
        
        await _accountRepository.DeleteUserAccountByIdAsync(new Guid(request.Id));

        return new Empty();
    }
}