using AutoMapper;
using Protos.Transaction;
using TransactionEntity = TransactionService.Entities.Transaction;
using TransactionProto = Protos.Transaction.Transaction;

namespace TransactionService.Mappers
{
    public class TransactionMapper : Profile
    {
        public TransactionMapper()
        {
            CreateMap<TransactionEntity, TransactionProto>();
            CreateMap<AddTransactionRequest, TransactionEntity>();
            CreateMap<UpdateTransactionRequest, TransactionEntity>();
            CreateMap<DeleteTransactionRequest, TransactionEntity>();
        }
    }
}
