#For teh "on duplicate key" clause to work you either need to rely on the primary key being unique or a unique
#index on the columns specified in the "on duplicate key" clause need to have a unique index. 

insert into invest.inv_category(category_desc) values('Stock') on duplicate key update category_desc='Stock';
insert into invest.inv_category(category_desc) values('Bond') on duplicate key update category_desc='Bond';
insert into invest.inv_category(category_desc) values('Cash') on duplicate key update category_desc='Cash';

insert into invest.investor(first_nm, last_nm) values('Fred', 'Flinstone') on duplicate key update first_nm='Fred', last_nm='Flintstone';

insert into invest.broker(broker_nm) values('Ally') on duplicate key update broker_nm='Ally';


insert into invest.inv_acct_class(broker_id, inv_acct_class_nm, taxable_ind) 
values((select id from invest.broker where broker_nm='Ally'),'Taxable',1) on duplicate key update 
broker_id=values(broker_id), inv_acct_class_nm='Ally', taxable_ind=1;
