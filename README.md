# Full-Stack-Django-React
This is a full stack application build with React and Django

## Get Started

1. Install Django and djangorestframework
2. **Install [Node 8](https://nodejs.org)** or newer. Need to run multiple versions of Node? Use [nvm](https://github.com/creationix/nvm) or [nvm-windows](https://github.com/coreybutler/nvm-windows)(https://github.com/coryhouse/pluralsight-redux-starter/archive/master.zip)
3. **Navigate to this project's root directory on the command line.**
4. **Install Node Packages.** - `npm install`
5. **Install [React developer tools](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en)
6. Having issues? See below.

## Having Issues? Try these things first:

1. Run `npm install` - If you forget to do this, you'll get an error when you try to start the app later.
2. Don't run the project from a symbolic link. It will cause issues with file watches.
3. Delete any .eslintrc in your user directory and disable any ESLint plugin / custom rules within your editor since these will conflict with the ESLint rules defined in the course.
4. On Windows? Open your console as an administrator. This will assure the console has the necessary rights to perform installs.
5. Ensure you do not have NODE_ENV=production in your env variables as it will not install the devDependencies. To check run this on the command line: `set NODE_ENV`. If it comes back as production, you need to clear this env variable.
6. Nothing above work? Delete your node_modules folder and re-run npm install.

### Production Dependencies

| **Dependency**   | **Use**                                              |
| ---------------- | ---------------------------------------------------- |
| bootstrap        | CSS Framework                                        |
| django           | Python Web FrameWork                                       |
| djangorestframework |a powerful and flexible toolkit for building Web API|
| prop-types       | Declare types for props passed into React components |
| react            | React library                                        |
| react-dom        | React library for DOM rendering                      |
| react-redux      | Connects React components to Redux                   |
| react-router-dom | React library for routing                            |

### Development Dependencies

| **Dependency**          | **Use**                                                          |
| ----------------------- | ---------------------------------------------------------------- |
| @babel/core             | Transpiles modern JavaScript so it runs cross-browser            |
| babel-loader            | Add Babel support to Webpack                                     |
| babel-preset-react-app  | Babel preset for working in React. Used by create-react-app too. |
| webpack                 | Bundler with plugin ecosystem and integrated dev server          |
| webpack-bundle-analyzer | Generate report of what's in the app's production bundle         |
| webpack-cli             | Run Webpack via the command line                                 |
| webpack-dev-server      | Serve app via Webpack                                            |
