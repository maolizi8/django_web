
function rendFomatedJson(data,dom){
	//'#json_display'
    var options = {
        "dom": dom 
    };
    // var str=JSON.stringify(data);
    var jf = new JsonFormater(options); //创建对象
    jf.doFormat(data); //格式化json
}

function getQueryString(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i"); 
    var r = window.location.search.substr(1).match(reg); 
    if (r != null) return unescape(decodeURIComponent(r[2])); 
    //if (r != null) return unescape(r[2]); 
    return null; 
}

function ajaxquery_foralert(req_url,json_param,type,func){
	$.ajax({
        type: type,
        url:req_url,
        data: json_param,
        contentType:"application/x-www-form-urlencoded",
        success: function(result){
        	func(result)
        },
        error:function (error) {
            console.log(error);
            layer.alert(error);
        }
    });
}

function ajaxquery_forrender(req_url,json_param,type,func){
	$.ajax({
        type: type,
        url:req_url,
        data: json_param,
        contentType:"application/x-www-form-urlencoded",
        success: function(result){
        	//console.log(result);
        	func(result)
        },
        error:function (error) {
            console.log(error);
            layer.msg(error);
        }
    });
}

function serialize_to_json(data){
	var obj=data.split('&')
	var data_json={}
	for(var i=0;i<obj.length;i++){
		key_v=obj[i].split('=')
		data_json[key_v[0]]=key_v[1]
	}
	return data_json
}

//function view_job_params(id){
//	
//	$.ajax({
//        type: 'post',
//        method: 'POST',
//        url: '/jobs/view_job_params/',
//        data: {'id':id},
//        contentType:"application/x-www-form-urlencoded",
//        success: function(result){
//        	var data = JSON.parse(result)
//        	console.log(data)
//        	//var html='<div style=""><form class="form-horizontal" role="form" id="">'
//        	var html='<div class="space-4"></div>'
//        	for(var i=0;i<data.length;i++){
//        		html+='<div class="form-group">'
//        		html+='<label class="col-md-3 control-label" for="addcase_suite"> <span class="required">*</span>'+data[i].fields.name+'：</label>'
//        		html+='<div class="col-md-8 col-sm-8">'
//        		
//        		if(data[i].fields.param_type=='ChoiceParameterDefinition'){
//        			html+='<select name="addcase_suite" id="'+data[i].fields.name+'" class="form-control">'
//        			options=data[i].fields.choices.split(';')
//        			console.log(options)
//        			for(var j=0;j<options.length;j++){
//        				console.log(options[j])
//        				html+='<option value="'+(options[j]||'')+'">'+(options[j]||'全部')+'</option>'
//        			}
//        			html+='</select>'
//        		}else if(data[i].fields.param_type=='StringParameterDefinition'){
//        			html+='<input type="text" id="'+data[i].fields.name+'" class="form-control" placeholder="请输入参数值" value="'+(data[i].fields.param_default||'')+'">'
//        		}
//	        	html+='</div>'
//	        	html+='</div>'
//        	}
//        	
//        	$('#params_form').html(html)
//        	$('#view_params').modal({
//				backdrop: 'static',
//				show: 'true'
//			})
//        },
//        error:function (error) {
//            console.log(error);
//            layer.alert(error);
//        }
//    }); 
//}