using AccountService.Repositories;
using AutoMapper;
using Grpc.Core;
using Protos.Account;
using AccountEntity = AccountService.Entities.Account;
using AccountProto = Protos.Account.Account;


namespace AccountService.Services;

public class AccountService : Protos.Account.AccountService.AccountServiceBase
{
    private readonly IRepository _repository;
    private readonly IMapper _mapper;

    public AccountService(IRepository repository, IMapper mapper)
    {
        _repository = repository;
        _mapper = mapper;
    }

    public override async Task<AccountsResponse> GetUserAccounts(GetUserAccountsRequest request, ServerCallContext context)
    {
        var dbAccounts = await _repository.GetAllUserAccountsAsync(request.UserId);

        var accounts = _mapper.Map<List<AccountProto>>(dbAccounts);
        var accountsResponse = new AccountsResponse();
        accountsResponse.Accounts.AddRange(accounts);

        context.Status = new Status(StatusCode.OK, "");
        return accountsResponse;
    }

    public override async Task<AccountResponse> GetAccountById(GetAccountByIdRequest request,
        ServerCallContext context)
    {
        var dbAccount = await _repository.GetAccountByIdAsync(request.Id);

        if (dbAccount == null)
        {
            throw new RpcException(new Status(StatusCode.NotFound, $"Account with Id {request.Id} does not exist."));
        }

        var account = _mapper.Map<AccountProto>(dbAccount);
        var accountResponse = new AccountResponse()
        {
            Account = account,
        };

        context.Status = new Status(StatusCode.OK, "");
        return accountResponse;
    }

    public override async Task<AccountResponse> CreateAccount(AddAccountRequest request,
        ServerCallContext context)
    {
        var newAccount = _mapper.Map<AccountEntity>(request);
        newAccount.Balance = 0;

        var dbAccount = await _repository.AddAccountAsync(newAccount);

        var account = _mapper.Map<AccountProto>(dbAccount);
        var accountResponse = new AccountResponse()
        {
            Account = account,
        };

        context.Status = new Status(StatusCode.OK, "");
        return accountResponse;
    }

    public override async Task<AccountResponse> UpdateAccount(UpdateAccountRequest request,
        ServerCallContext context)
    {
        var checkAccount = await _repository.GetAccountByIdAsync(request.Id);

        if (checkAccount == null)
        {
            throw new RpcException(new Status(StatusCode.NotFound, $"Account with Id {request.Id} does not exist."));
        }

        var updateAccount = _mapper.Map<AccountEntity>(request);
        var dbAccount = await _repository.UpdateAccountAsync(updateAccount);
        var account = _mapper.Map<AccountProto>(dbAccount);
        var accountResponse = new AccountResponse()
        {
            Account = account,
        };

        context.Status = new Status(StatusCode.OK, "");
        return accountResponse;
    }

    public override async Task<AccountResponse> DeleteAccount(DeleteAccountRequest request,
        ServerCallContext context)
    {
        var checkAccount = await _repository.GetAccountByIdAsync(request.Id);

        if (checkAccount == null)
        {
            throw new RpcException(new Status(StatusCode.NotFound, $"Account with Id {request.Id} does not exist."));
        }

        await _repository.DeleteAccountByIdAsync(checkAccount);

        context.Status = new Status(StatusCode.OK, "");
        return new AccountResponse();
    }
}