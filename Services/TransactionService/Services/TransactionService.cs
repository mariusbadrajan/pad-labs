using AutoMapper;
using Grpc.Core;
using Protos.Transaction;
using TransactionService.Repositories;
using TransactionEntity = TransactionService.Entities.Transaction;
using TransactionProto = Protos.Transaction.Transaction;

namespace TransactionService.Services;

public class TransactionService : Protos.Transaction.TransactionService.TransactionServiceBase
{
    private readonly IRepository _repository;
    private readonly IMapper _mapper;

    public TransactionService(IRepository repository, IMapper mapper)
    {
        _repository = repository;
        _mapper = mapper;
    }

    public override async Task<TransactionsResponse> GetUserTransactions(GetUserTransactionsRequest request, ServerCallContext context)
    {
        var dbTransactions = await _repository.GetAllUserTransactionsAsync(request.UserId);

        var transactions = _mapper.Map<List<TransactionProto>>(dbTransactions);
        var transactionsResponse = new TransactionsResponse();
        transactionsResponse.Transactions.AddRange(transactions);

        context.Status = new Status(StatusCode.OK, "");
        return transactionsResponse;
    }

    public override async Task<TransactionsResponse> GetAccountTransactions(GetAccountTransactionsRequest request,
        ServerCallContext context)
    {
        var dbTransactions = await _repository.GetAllAccountTransactionsAsync(request.AccountId);

        var transactions = _mapper.Map<List<TransactionProto>>(dbTransactions);
        var transactionsResponse = new TransactionsResponse();
        transactionsResponse.Transactions.AddRange(transactions);

        context.Status = new Status(StatusCode.OK, "");
        return transactionsResponse;
    }

    public override async Task<TransactionResponse> GetTransactionById(GetTransactionByIdRequest request,
        ServerCallContext context)
    {
        var dbTransaction = await _repository.GetTransactionByIdAsync(request.Id);

        if (dbTransaction == null)
        {
            throw new RpcException(new Status(StatusCode.NotFound, $"Transaction with Id {request.Id} does not exist."));
        }

        var transaction = _mapper.Map<TransactionProto>(dbTransaction);
        var transactionResponse = new TransactionResponse()
        {
            Transaction = transaction,
        };

        context.Status = new Status(StatusCode.OK, "haha");
        return transactionResponse;
    }

    public override async Task<TransactionResponse> CreatePaymentTransaction(AddTransactionRequest request,
        ServerCallContext context)
    {
        var newTransaction = _mapper.Map<TransactionEntity>(request);
        newTransaction.Type = "Payment";
        newTransaction.Status = "Completed";

        var dbTransaction = await _repository.AddTransactionAsync(newTransaction);

        var transaction = _mapper.Map<TransactionProto>(dbTransaction);
        var transactionResponse = new TransactionResponse()
        {
            Transaction = transaction,
        };

        context.Status = new Status(StatusCode.OK, "");
        return transactionResponse;
    }

    public override async Task<TransactionResponse> UpdateTransaction(UpdateTransactionRequest request,
        ServerCallContext context)
    {
        var checkTransaction = await _repository.GetTransactionByIdAsync(request.Id);

        if (checkTransaction == null)
        {
            throw new RpcException(new Status(StatusCode.NotFound, $"Transaction with Id {request.Id} does not exist."));
        }

        var updateTransaction = _mapper.Map<TransactionEntity>(request);
        var dbTransaction = await _repository.UpdateTransactionAsync(updateTransaction);
        var transaction = _mapper.Map<TransactionProto>(dbTransaction);
        var transactionResponse = new TransactionResponse()
        {
            Transaction = transaction,
        };

        context.Status = new Status(StatusCode.OK, "");
        return transactionResponse;
    }

    public override async Task<TransactionResponse> DeleteTransaction(DeleteTransactionRequest request,
        ServerCallContext context)
    {
        var checkTransaction = await _repository.GetTransactionByIdAsync(request.Id);

        if (checkTransaction == null)
        {
            throw new RpcException(new Status(StatusCode.NotFound, $"Transaction with Id {request.Id} does not exist."));
        }

        await _repository.DeleteTransactionByIdAsync(checkTransaction);

        context.Status = new Status(StatusCode.OK, "");
        return new TransactionResponse();
    }
}