const webpack = require("webpack")
const path = require("path")
const ExtractTextPlugin = require("extract-text-webpack-plugin")

// export init
module.exports = {
    entry: {
        main: path.resolve('./main/js/main.js'),
        event: path.resolve('./event/js/main.js'),
        guest: path.resolve('./guest/js/main.js'),
        layout: path.resolve('./layout/js/main.js'),
        raffler: path.resolve('./raffler/js/main.js'),
    },

    // compiled bundle location
    output: {
        path: __dirname,
        filename: "./[name]/static/compiled/js/[name].js"
    },

    plugins: [
        new webpack.optimize.CommonsChunkPlugin({
            name: "shared",
            filename: "./main/static/compiled/js/shared.js"
        }),
        new ExtractTextPlugin("./[name]/static/compiled/css/[name].css"),
        new webpack.ProvidePlugin({
            $: "jquery",
            jQuery: "jquery",
            "window.jQuery": "jquery'",
            "window.$": "jquery"
        })
    ],

    module: {
        loaders: [
            {
                test: /\.(scss|sass)$/,
                use: ExtractTextPlugin.extract({
                    fallback: 'style-loader',
                    //resolve-url-loader may be chained before sass-loader if necessary
                    use: ['css-loader', 'postcss-loader', 'sass-loader']
                }),

            },
            {
                test: /\.(scss|sass)$/,
                loader: 'sass-loader',
                options: {
                    sourceMap: true
                }
            },
            {
                test: /\.css$/,
                use: ExtractTextPlugin.extract({
                    //resolve-url-loader may be chained before sass-loader if necessary
                    use: ['style-loader', 'css-loader', 'postcss-loader']
                })
            },

            {
                test: /\.vue$/, // a regex for matching all files that end in `.vue`
                loader: 'vue-loader',   // loader to use for matched files
                options: {

                    loaders: {
                        scss: ExtractTextPlugin.extract({
                            use: 'css-loader!sass-loader',
                            fallback: 'vue-style-loader'
                        }),
                        sass: ExtractTextPlugin.extract({
                            use: 'css-loader!sass-loader?indentedSyntax',
                            fallback: 'vue-style-loader'
                        })
                    }
                }
            },
            {
                // use babel-loader for *.js files
                test: /\.js$/,
                loader: 'babel-loader',
                // important: exclude files in node_modules
                // otherwise it's going to be really slow!
                exclude: /node_modules/
            },

            {
                test: /\.(eot|svg|ttf|woff|woff2)$/,
                loader: 'file-loader?name=./fonts/[name].[ext]'
            },
            {
                test: /\.(ogg|mp3|wav|mpe?g)$/i,
                use: [{
                    loader: 'url-loader',
                    options: {}
                }]
            },
            {
                test: /\.(png|jp(e*)g|svg)$/i,
                use: [{
                    loader: 'url-loader',
                    options: {}
                }]
            },
            {
                test: /\.exec\.js$/,
                use: ['script-loader']
            },
        ]
    },

    resolve: {
        extensions: ['.js', '.vue'],
        alias: {
            'vue': 'vue/dist/vue.common.js'
        },
        // alias: {'vue$': 'vue/dist/vue.esm.js'},
        // extensions: ['.js', '.vue'], // this string resolve your problem
    }
}