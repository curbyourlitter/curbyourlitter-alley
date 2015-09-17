var ratings = require('curbyourlitter-pavement');

function init() {
    ratings.init({
        appDOMId: 'app',
        rootPath: '/streetratings/'
    });
}

if (document.readyState !== 'loading') {
    init();
}
else {
    document.addEventListener('DOMContentLoaded', init);
}
