Ext.Loader.setConfig({
   enabled: true
});

Ext.Loader.setPath('Ext.ux', '/static/ux');
Ext.Loader.setPath('Ext.ux.plugin.FancyScroll', '/static/ux/plugin/FancyScroll/FancyScroll.js');
Ext.Loader.setPath('Ext.ux.plugin.minimize', '/static/ux/plugin/ExtJS-Minimize/');
Ext.Loader.setPath('Ext.ux.list', '/static/ux/extjs-smartlist/');

var _app = Ext.create('Ext.app.Application',{
	name: 'Inatel',
    autoCreateViewport: true,
    appFolder: '/static/app',

    controllers: [
        'from-grid',
    ],
    
    launch: function() {
        Ext.require([
            'Netvision.util.NotificationManager',
            'Ext.ux.CheckColumn'
        ]);

        this.setupOverrides();
    },

    setupOverrides: function(){
        Ext.override(Ext.form.field.ComboBox, {
            /*
             * Retorna o record referente ao valor selecionado.
             * Exemplo: http://jsfiddle.net/marcio0/tVhac/
             */
            getRecord: function(){
                var me = this;

                if(!me.store || !me.value){
                    return null;
                }

                return me.store.getById(me.getValue());
            }
        });
    }
});


