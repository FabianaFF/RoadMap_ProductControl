	Ext.onReady(function(){

		var store = new Ext.data.JsonStore({
		    // store configs
		    storeId: 'ProductSpecStore',

		    proxy: {
		        type: 'ajax',
		        url: '/product/product_spec',
		        reader: {
		            type: 'json',
		            //root: 'products',
		            idProperty: 'id'
		        }
		    },

		    //alternatively, a Ext.data.Model name can be given (see Ext.data.Store for an example)
		    fields: [ {name:'id', type: 'int'}, {name:'name', type:'string'}]
		});
	store.load();
	
	var grid = new Ext.grid.GridPanel({
			title: 'Product Spec',			
			store: store,
	        columns: [	     
				{
					width: 40,
				    renderer: function (v, m, r) {
				        var id = Ext.id();
				        Ext.defer(function () {
				            Ext.widget('button', {
				            	href: 'http://localhost:8000/lista2/detail/'+ r.get('id'),
				                renderTo: id,
				                text: 'X',
				                width: 25,
				                handler: function () {
				                	if (this.href) {
				                    		window.location.href = this.href;
				                    	} 
				                }
				            });
				        }, 50);
				        return Ext.String.format('<div id="{0}"></div>', id);
				    }
				},
				{
					width: 70,
				    renderer: function (v, m, r) {
				        var id = Ext.id();
				        Ext.defer(function () {
				        	Ext.create('Ext.button.Button',{				            	
				                renderTo: id,
				                text: 'Editar',
				                width: 55,
				                listeners : {
				                    click: function(btn, e, eOpts) {				                     
				                    	loadDataToChange(r.get('id'), r.get('name'));
				                    }
				                }
				            });
				        }, 50);
				        return Ext.String.format('<div id="{0}"></div>', id);
				    }
				},								
	            {header: "Id", width: 60, dataIndex: 'id', sortable: true, hidden: true},
	            {header: "Name", width: 170, dataIndex: 'name', sortable: true,
	            	renderer: function (value, metaData, record, row, col, store, gridView) {
	            		 var rec = store.getAt(row);            		   
	                     return Ext.String.format('<a href="http://localhost:8000/lista2/{0}">{1}</a>',rec.get('id'), value);
	                 }
	            }
	        ],
	        renderTo: Ext.getBody(),
	        width:300,
	        height:200
	    });
	
	var win;
	
	function loadDataToChange(id, name){
		
	    if (!win) {
	        var form = Ext.widget('form', {
	        	method: 'PUT',
	            layout: {
	                type: 'vbox',
	                align: 'stretch'
	            },
	            border: false,
	            bodyPadding: 10,

	            fieldDefaults: {
	                labelAlign: 'top',
	                labelWidth: 100,
	                labelStyle: 'font-weight:bold'
	            },
	            defaults: {
	                margins: '0 0 10 0'
	            },

	            items: [ {
	                xtype: 'textfield',
	                fieldLabel: 'Id',	                
	                value: id,
	                hidden: true,
	                allowBlank: false
	            }, {
	                xtype: 'textfield',
	                fieldLabel: 'Name',	                
	                value: name,
	                allowBlank: false
	            }],

	            buttons: [{
	                text: 'Cancel',
	                handler: function() {
	                    this.up('form').getForm().reset();
	                    this.up('window').hide();
	                }
	            }, {
	                text: 'Send',
	                handler: function() {
	                    if (this.up('form').getForm().isValid()) {
	                        this.up('form').getForm().reset();
	                        this.up('window').hide();
	                        Ext.MessageBox.alert('Thank you!', 'Your inquiry has been sent. We will respond as soon as possible.');
	                    }
	                }
	            }]
	        });

	        win = Ext.widget('window', {
	            title: 'Product Spec',
	            closeAction: 'hide',
	            width: 400,
	            height: 400,
	            minHeight: 400,
	            layout: 'fit',
	            resizable: true,
	            modal: true,
	            items: form
	        });
	        
	        win.show();
	    }
	    
	}
	});