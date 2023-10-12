using Grpc.Core;
using TransactionService.Protos;
using TransactionService.Repositories;
using TransactionServices = TransactionService.Protos.TransactionService;

namespace TransactionService.Services;

public class TransactionService : TransactionServices.TransactionServiceBase
{
    private readonly ITransactionRepository _transactionRepository;

    public TransactionService(ITransactionRepository transactionRepository)
    {
        _transactionRepository = transactionRepository;
    }
    
    public override async Task<Transactions> GetTransactions(Empty request, ServerCallContext context)
    {
        var dbTransactions = await _transactionRepository.GetAllTransactionsAsync();
        
        var transactions = new Transactions();
        foreach (var transaction in dbTransactions)
        {
            transactions.AllTransactions.Add(new Transaction
            {
                Id = transaction.Id.ToString("D"),
                UserId = transaction.UserId.ToString("D"),
                Type = transaction.Type,
                Amount = transaction.Amount,
                Description = transaction.Description,
                Status = transaction.Status
            });
        }

        return transactions;
    }

    public override async Task<Transactions> GetTransactionByUserId(GetTransactionsByUserIdRequest request,
        ServerCallContext context)
    {
        var dbTransactions = await _transactionRepository.GetAllTransactionsByUserIdAsync(new Guid(request.UserId));
        
        var transactions = new Transactions();
        foreach (var transaction in dbTransactions)
        {
            transactions.AllTransactions.Add(new Transaction
            {
                Id = transaction.Id.ToString("D"),
                UserId = transaction.UserId.ToString("D"),
                Type = transaction.Type,
                Amount = transaction.Amount,
                Description = transaction.Description,
                Status = transaction.Status
            });
        }

        return transactions;
    }

    public override async Task<Transaction> GetTransactionById(GetTransactionByIdRequest request,
        ServerCallContext context)
    {
        var dbTransaction = await _transactionRepository.GetTransactionByIdAsync(new Guid(request.Id));

        var transaction = new Transaction
        {
            Id = dbTransaction.Id.ToString("D"),
            UserId = dbTransaction.UserId.ToString("D"),
            Type = dbTransaction.Type,
            Amount = dbTransaction.Amount,
            Description = dbTransaction.Description,
            Status = dbTransaction.Status
        };

        return transaction;
    }

    public override async Task<Transaction> AddTransaction(AddTransactionRequest request,
        ServerCallContext context)
    {
        var dbTransaction = new Entities.Transaction
        {
            Id = new Guid(request.Transaction.Id),
            UserId = new Guid(request.Transaction.UserId),
            Type = request.Transaction.Type,
            Amount = request.Transaction.Amount,
            Description = request.Transaction.Description,
            Status = request.Transaction.Status
        };

        var transaction = await _transactionRepository.AddTransactionAsync(dbTransaction);

        return request.Transaction;
    }

    public override async Task<Transaction> UpdateTransaction(UpdateTransactionRequest request,
        ServerCallContext context)
    {
        var dbTransaction = new Entities.Transaction
        {
            Id = new Guid(request.Transaction.Id),
            UserId = new Guid(request.Transaction.UserId),
            Type = request.Transaction.Type,
            Amount = request.Transaction.Amount,
            Description = request.Transaction.Description,
            Status = request.Transaction.Status
        };

        var transaction = await _transactionRepository.UpdateTransactionAsync(dbTransaction);

        return request.Transaction;
    }
    
    public override async Task<Empty> DeleteTransaction(DeleteTransactionRequest request,
        ServerCallContext context)
    {
        
        await _transactionRepository.DeleteTransactionByIdAsync(new Guid(request.Id));

        return new Empty();
    }
}