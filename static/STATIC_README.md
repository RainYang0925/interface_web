# Static Media

We are using `gulp` and `npm` for our static build process.

Do NOT edit anything in the `dist/` directory.

Local development uses media from `dist/` and we are firm believers in building
static assets and committing them to the repo before deployments. This way we
always are testing and exercise exactly what will be served in production. It
also makes our deployment simpler.

Windows配置：
全局安装 gulp 命令 `npm install -g gulp` 
本地项目目录也要安装 `npm install gulp`
提示缺少 `del` 模块 和下面的：

```
npm WARN package.json @ No license field.
npm WARN deprecated minimatch@2.0.10: Please update to minimatch 3.0.2 or higher to avoid a RegExp DoS issue
npm WARN deprecated minimatch@0.2.14: Please update to minimatch 3.0.2 or higher to avoid a RegExp DoS issue
npm WARN deprecated graceful-fs@1.2.3: graceful-fs v3.0.0 and before will fail on node releases >= v7.0. Please update to graceful-fs@^4.0.0 as soon as possible. Use 'npm ls graceful-fs' to find it in the tree.

npm ERR! missing: bootstrap@^3.3.7, required by @
npm ERR! missing: font-awesome@^4.6.3, required by @
npm ERR! missing: jquery@^2.2.4, required by @
```

运行以下命令解决：

```
npm install -g minimatch@^3.0.2
npm install -g graceful-fs@^4.0.0
npm install
```
或者试试这个：

```
# first uninstall gulp globally
npm uninstall gulp -g

# uninstall from your project directory, or delete node_modules if you need a coffee break
npm uninstall gulp

# install the latest Gulp 4 CLI tools globally
npm install gulpjs/gulp-cli -g
```


