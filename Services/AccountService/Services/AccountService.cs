using AccountService.Proto;
using AccountService.Repositories;
using Grpc.Core;
using System.Data.Common;
using AccountServices = AccountService.Proto.AccountService;

namespace AccountService.Services;

public class AccountService : AccountServices.AccountServiceBase
{
    private readonly IRepository _repository;
    private readonly int _maxTransactionAmount = 100;

    public AccountService(IRepository repository)
    {
        _repository = repository;
    }

    public override async Task<AccountsResponse> GetUserAccounts(GetUserAccountsRequest request, ServerCallContext context)
    {
        var dbAccounts = _repository.GetAllUserAccountsAsync(request.UserId);
        bool transactionCompletedInTime = await Task.WhenAny(dbAccounts, Task.Delay(_maxTransactionAmount)) == dbAccounts;

        if (transactionCompletedInTime)
        {
            if (!dbAccounts.Result.Any())
            {
                return new AccountsResponse() { Message = "Collection is empty" };
            }

            var accounts = new AccountsResponse();
            foreach (var dbAccount in dbAccounts.Result)
            {
                accounts.Accounts.Add(new AccountResponse
                {
                    Id = dbAccount.Id,
                    UserId = dbAccount.UserId,
                    Balance = dbAccount.Balance,
                });
            }
            accounts.Message = "Ok";

            return accounts;
        }
        else
        {
            return new AccountsResponse() { Message = "Request timeout" };
        }
    }

    public override async Task<AccountResponse> GetAccountById(GetAccountByIdRequest request,
        ServerCallContext context)
    {
        var dbAccount = _repository.GetAccountByIdAsync(request.Id);
        bool transactionCompletedInTime = await Task.WhenAny(dbAccount, Task.Delay(_maxTransactionAmount)) == dbAccount;

        if (transactionCompletedInTime)
        {
            if (dbAccount.Result == null)
            {
                return new AccountResponse() { Message = "Not found" };
            }

            var account = new AccountResponse
            {
                Id = dbAccount.Result.Id,
                UserId = dbAccount.Result.UserId,
                Balance = dbAccount.Result.Balance,
                Message = "Ok"
            };

            return account;
        }
        else
        {
            return new AccountResponse() { Message = "Request timeout" };
        }
    }

    public override async Task<AccountResponse> CreateAccount(AddAccountRequest request,
        ServerCallContext context)
    {
        var addDbAccount = new Entities.Account
        {
            UserId = request.Account.UserId,
            Balance = 0
        };

        var dbAccount = _repository.AddAccountAsync(addDbAccount);
        bool transactionCompletedInTime = await Task.WhenAny(dbAccount, Task.Delay(_maxTransactionAmount)) == dbAccount;

        if (transactionCompletedInTime)
        {
            var account = new AccountResponse
            {
                Id = dbAccount.Result.Id,
                UserId = dbAccount.Result.UserId,
                Balance = dbAccount.Result.Balance,
                Message = "Ok"
            };

            return account;
        }
        else
        {
            return new AccountResponse() { Message = "Request timeout" };
        }
    }

    public override async Task<AccountResponse> UpdateAccount(UpdateAccountRequest request,
        ServerCallContext context)
    {
        var checkAccount = await _repository.GetAccountByIdAsync(request.Account.Id);

        if (checkAccount == null)
        {
            return new AccountResponse() { Message = "Not found" };
        }

        var updateDbAccount = new Entities.Account
        {
            Id = request.Account.Id,
            UserId = request.Account.UserId,
            Balance = request.Account.Balance
        };

        var dbAccount = _repository.UpdateAccountAsync(updateDbAccount);
        bool transactionCompletedInTime = await Task.WhenAny(dbAccount, Task.Delay(_maxTransactionAmount)) == dbAccount;

        if (transactionCompletedInTime)
        {
            var account = new AccountResponse
            {
                Id = dbAccount.Result.Id,
                UserId = dbAccount.Result.UserId,
                Balance = dbAccount.Result.Balance,
                Message = "Ok"
            };

            return account;
        }
        else
        {
            return new AccountResponse() { Message = "Request timeout" };
        }
    }

    public override async Task<AccountResponse> DeleteAccount(DeleteAccountRequest request,
        ServerCallContext context)
    {
        var checkAccount = _repository.GetAccountByIdAsync(request.Id);
        bool transactionCompletedInTime = await Task.WhenAny(checkAccount, Task.Delay(_maxTransactionAmount)) == checkAccount;

        if (transactionCompletedInTime)
        {
            if (checkAccount.Result == null)
            {
                return new AccountResponse() { Message = "Not found" };
            }
        }
        else
        {
            return new AccountResponse() { Message = "Request timeout" };
        }

        await _repository.DeleteAccountByIdAsync(request.Id);

        return new AccountResponse() { Message = "Ok" };
    }
}