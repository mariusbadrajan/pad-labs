using Grpc.Core;
using TransactionService.Protos;
using TransactionService.Repositories;
using TransactionServices = TransactionService.Protos.TransactionService;

namespace TransactionService.Services;

public class Service : TransactionServices.TransactionServiceBase
{
    private readonly IRepository _repository;
    private readonly int _maxTransactionAmount = 100;

    public Service(IRepository repository)
    {
        _repository = repository;
    }

    public override async Task<TransactionsResponse> GetUserTransactions(GetUserTransactionsRequest request, ServerCallContext context)
    {
        var dbTransactions = _repository.GetAllUserTransactionsAsync(request.UserId);
        bool transactionCompletedInTime = await Task.WhenAny(dbTransactions, Task.Delay(_maxTransactionAmount)) == dbTransactions;

        if (transactionCompletedInTime)
        {
            if (!dbTransactions.Result.Any())
            {
                return new TransactionsResponse() { Message = "Collection is empty" };
            }

            var transactions = new TransactionsResponse();
            foreach (var dbTransaction in dbTransactions.Result)
            {
                transactions.Transactions.Add(new TransactionResponse
                {
                    Id = dbTransaction.Id,
                    UserId = dbTransaction.UserId,
                    AccountId = dbTransaction.AccountId,
                    Type = dbTransaction.Type,
                    Amount = dbTransaction.Amount,
                    Status = dbTransaction.Status,
                });
            }
            transactions.Message = "Ok";

            return transactions;
        }
        else
        {
            return new TransactionsResponse() { Message = "Request timeout" };
        }
    }

    public override async Task<TransactionsResponse> GetAccountTransactions(GetAccountTransactionsRequest request,
        ServerCallContext context)
    {
        var dbTransactions = _repository.GetAllAccountTransactionsAsync(request.AccountId);
        bool transactionCompletedInTime = await Task.WhenAny(dbTransactions, Task.Delay(_maxTransactionAmount)) == dbTransactions;

        if (transactionCompletedInTime)
        {
            if (!dbTransactions.Result.Any())
            {
                return new TransactionsResponse() { Message = "Collection is empty" };
            }

            var transactions = new TransactionsResponse();
            foreach (var dbTransaction in dbTransactions.Result)
            {
                transactions.Transactions.Add(new TransactionResponse
                {
                    Id = dbTransaction.Id,
                    UserId = dbTransaction.UserId,
                    AccountId = dbTransaction.AccountId,
                    Type = dbTransaction.Type,
                    Amount = dbTransaction.Amount,
                    Status = dbTransaction.Status,
                });
            }
            transactions.Message = "Ok";

            return transactions;
        }
        else
        {
            return new TransactionsResponse() { Message = "Request timeout" };
        }
    }

    public override async Task<TransactionResponse> GetTransactionById(GetTransactionByIdRequest request,
        ServerCallContext context)
    {
        var dbTransaction = _repository.GetTransactionByIdAsync(request.Id);
        bool transactionCompletedInTime = await Task.WhenAny(dbTransaction, Task.Delay(_maxTransactionAmount)) == dbTransaction;

        if (transactionCompletedInTime)
        {
            if (dbTransaction.Result == null)
            {
                return new TransactionResponse() { Message = "Not found" };
            }

            var transaction = new TransactionResponse
            {
                Id = dbTransaction.Result.Id,
                UserId = dbTransaction.Result.UserId,
                AccountId = dbTransaction.Result.AccountId,
                Type = dbTransaction.Result.Type,
                Amount = dbTransaction.Result.Amount,
                Status = dbTransaction.Result.Status,
                Message = "Ok"
            };

            return transaction;
        }
        else
        {
            return new TransactionResponse() { Message = "Request timeout" };
        }
    }

    public override async Task<TransactionResponse> CreatePaymentTransaction(AddTransactionRequest request,
        ServerCallContext context)
    {
        var addDbTransaction = new Entities.Transaction
        {
            UserId = request.Transaction.UserId,
            AccountId = request.Transaction.AccountId,
            Type = "Payment",
            Amount = request.Transaction.Amount,
            Status = "Completed"
        };

        var dbTransaction = _repository.AddTransactionAsync(addDbTransaction);
        bool transactionCompletedInTime = await Task.WhenAny(dbTransaction, Task.Delay(_maxTransactionAmount)) == dbTransaction;

        if (transactionCompletedInTime)
        {
            var transaction = new TransactionResponse
            {
                Id = dbTransaction.Result.Id,
                UserId = dbTransaction.Result.UserId,
                AccountId = dbTransaction.Result.AccountId,
                Type = dbTransaction.Result.Type,
                Amount = dbTransaction.Result.Amount,
                Status = dbTransaction.Result.Status,
                Message = "Ok"
            };

            return transaction;
        }
        else
        {
            return new TransactionResponse() { Message = "Request timeout" };
        }
    }

    public override async Task<TransactionResponse> UpdateTransaction(UpdateTransactionRequest request,
        ServerCallContext context)
    {
        var checkTransaction = await _repository.GetTransactionByIdAsync(request.Transaction.Id);

        if (checkTransaction == null)
        {
            return new TransactionResponse() { Message = "Not found" };
        }

        var updateDbTransaction = new Entities.Transaction
        {
            Id = request.Transaction.Id,
            UserId = request.Transaction.UserId,
            AccountId = request.Transaction.AccountId,
            Type = request.Transaction.Type,
            Amount = request.Transaction.Amount,
            Status = request.Transaction.Status
        };

        var dbTransaction = _repository.UpdateTransactionAsync(updateDbTransaction);
        bool transactionCompletedInTime = await Task.WhenAny(dbTransaction, Task.Delay(_maxTransactionAmount)) == dbTransaction;

        if (transactionCompletedInTime)
        {
            var transaction = new TransactionResponse
            {
                Id = dbTransaction.Result.Id,
                UserId = dbTransaction.Result.UserId,
                AccountId = dbTransaction.Result.AccountId,
                Type = dbTransaction.Result.Type,
                Amount = dbTransaction.Result.Amount,
                Status = dbTransaction.Result.Status,
                Message = "Ok"
            };

            return transaction;
        }
        else
        {
            return new TransactionResponse() { Message = "Request timeout" };
        }
    }

    public override async Task<TransactionResponse> DeleteTransaction(DeleteTransactionRequest request,
        ServerCallContext context)
    {
        var checkTransaction = _repository.GetTransactionByIdAsync(request.Id);
        bool transactionCompletedInTime = await Task.WhenAny(checkTransaction, Task.Delay(_maxTransactionAmount)) == checkTransaction;

        if (transactionCompletedInTime)
        {
            if (checkTransaction.Result == null)
            {
                return new TransactionResponse() { Message = "Not found" };
            }
        }
        else
        {
            return new TransactionResponse() { Message = "Request timeout" };
        }

        await _repository.DeleteTransactionByIdAsync(request.Id);

        return new TransactionResponse() { Message = "Ok" };
    }
}