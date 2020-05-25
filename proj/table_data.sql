#For the "on duplicate key" clause to work you either need to rely on the primary key being unique or a unique
#index on the columns specified in the "on duplicate key" clause need to have a unique index. 

insert into invest.inv_category(category_desc) values('Stock') on duplicate key update category_desc='Stock';
insert into invest.inv_category(category_desc) values('Bond') on duplicate key update category_desc='Bond';
insert into invest.inv_category(category_desc) values('Cash') on duplicate key update category_desc='Cash';

insert into invest.investor(first_nm, last_nm) values('Fred', 'Flinstone') on duplicate key update first_nm='Fred', last_nm='Flintstone';

insert into invest.broker(broker_nm) values('Ally') on duplicate key update broker_nm='Ally';


insert into invest.inv_acct_class(broker_id, inv_acct_class_nm, taxable_ind) 
values((select id from invest.broker where broker_nm='Ally'),'Stock',1) on duplicate key update 
broker_id=values(broker_id), inv_acct_class_nm='Stock', taxable_ind=1;

insert into invest.inv_category(category_desc) values('Stock') on duplicate key update category_desc='Stock';
insert into invest.inv_category(category_desc) values('Bond') on duplicate key update category_desc='Bond';
insert into invest.inv_category(category_desc) values('Cash') on duplicate key update category_desc='Cash';

#These non-domain tables should be populated without the UPSERT (on duplicate key) statement. I don't want to 
#implement the required unique index on this table: 
#insert into invest.symbols(inv_category_id, symbol_nm, description, official_symbol_ind, active_symbol_ind) values((select id from invest.inv_category where category_desc='Stock'),'AAPL','Apple stock',1,1);
#insert into invest.symbols(inv_category_id, symbol_nm, description, official_symbol_ind, active_symbol_ind) values((select id from invest.inv_category where category_desc='Stock'),'D','Dominion Energy stock',1,1);
#insert into invest.symbols(inv_category_id, symbol_nm, description, official_symbol_ind, active_symbol_ind) values((select id from invest.inv_category where category_desc='Stock'),'GOOGL','Google stock',1,1);
#insert into invest.symbols(inv_category_id, symbol_nm, description, official_symbol_ind, active_symbol_ind) values((select id from invest.inv_category where category_desc='Stock'),'JNJ','Johnson and Johnson stock',1,1);
#insert into invest.symbols(inv_category_id, symbol_nm, description, official_symbol_ind, active_symbol_ind) values((select id from invest.inv_category where category_desc='Stock'),'MSFT','Microsoft stock',1,1);
#insert into invest.symbols(inv_category_id, symbol_nm, description, official_symbol_ind, active_symbol_ind) values((select id from invest.inv_category where category_desc='Stock'),'T','AT&T stock',1,1);

