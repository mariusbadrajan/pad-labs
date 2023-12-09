using AutoMapper;
using Protos.Account;
using AccountEntity = AccountService.Entities.Account;
using AccountProto = Protos.Account.Account;

namespace AccountService.Mappers
{
    public class AccountMapper : Profile
    {
        public AccountMapper()
        {
            CreateMap<AccountEntity, AccountProto>();
            CreateMap<AddAccountRequest, AccountEntity>();
            CreateMap<UpdateAccountRequest, AccountEntity>();
            CreateMap<DeleteAccountRequest, AccountEntity>();
        }
    }
}
