Ext.onReady(function(){

		var store = new Ext.data.JsonStore({
		    // store configs
		    storeId: 'ProductStore',

		    proxy: {
		        type: 'ajax',
		        url: '/product',
		        reader: {
		            type: 'json',
		            //root: 'products',
		            idProperty: 'id'
		        }
		    },

		    //alternatively, a Ext.data.Model name can be given (see Ext.data.Store for an example)
		    fields: [ {name:'id', type: 'int'}, {name:'price', type: 'float'}, {name:'name', type:'string'}]
		});
	store.load();
	var sm = Ext.create('Ext.selection.CheckboxModel');
	var grid = new Ext.grid.GridPanel({
			title: 'Products ',
			selModel: sm,
	        store: store,
	        columns: [	            
				{
					width: 70,
				    renderer: function (v, m, r) {
				        var id = Ext.id();
				        Ext.defer(function () {
				            Ext.widget('button', {
				                renderTo: id,
				                text: 'Editar',
				                width: 55,
				                handler: function () { Ext.Msg.alert('Info', r.get('name')) }
				            });
				        }, 50);
				        return Ext.String.format('<div id="{0}"></div>', id);
				    }
				},
	            {header: "Id", width: 60, dataIndex: 'id', sortable: true, hidden: true},
	            {header: "Name", width: 120, dataIndex: 'name', sortable: true},
	            {header: "Price", width: 60, dataIndex: 'price', sortable: true}
	            
	        ],
	        renderTo: Ext.getBody(),
	        width:300,
	        height:200
	    });
	});