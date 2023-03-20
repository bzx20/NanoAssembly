const { defineConfig } = require('@vue/cli-service')
const VuetifyLoaderPlugin = require('vuetify-loader/lib/plugin')
module.exports = defineConfig({
    transpileDependencies: [
        'vuetify'
    ],
    devServer: {
        proxy: {
            '/api': {
                target: 'http://127.0.0.1:8100',
                changeOrigin: true,
                pathRewrite: {
                    '/api': '/api'
                }
            }
        }
    },
    configureWebpack: {
        plugins: [
            new VuetifyLoaderPlugin()
        ],
        optimization: {
            splitChunks: {
                cacheGroups: {
                    vuetify: {
                        test: /\/node_modules\/vuetify\//,
                        name: 'vuetify',
                        chunks: 'all',
                        enforce: true
                    }
                }
            }
        }
    }
})