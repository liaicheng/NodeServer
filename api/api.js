var http = require('http');
var request = require('request');

function hello(req,cb){
	console.log(req);
	console.log('iiii');
	var data;
	data = 'helloworld';
	cb(null,data);
	return 
}

function getUser(opt,cb){
	userid = opt.id;
}

function listing_from_top_school(option, cb){

  var opt = {"cd": {"paddress.city": "palo alto", "basic.status":"active" }, "doc_key":"prop", 
             "pj": { 
              "_id" : 0,
              "loc":1, 
              "paddress":1, 
              "basic":1, 
              "pub_id": 1, 
              "detail.pubcmt" : 1 ,
              "update.created_dtm":1,  
              "photos.thumbnail" : 1, 
              "transaction.mlsid":1
              },
              "st":{
                "update.created_dtm": -1
              },
              "lt": 20
            };
  base_api.queryData( opt, function(err, data){
    if(err){
      cb(err, null);
      return;
    }
    if( data.length == 0 ){
      cb({"error": "Can not find matching listing_from_top_school" }, null);
      return
    }
    
    cb( null, data );
  });

}

exports.hello = hello;
