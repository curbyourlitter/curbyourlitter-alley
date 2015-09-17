'use strict';

var gulp = require('gulp');
var del = require('del');
var path = require('path');

// Load plugins
var $ = require('gulp-load-plugins')();
var browserify = require('browserify');
var envify = require('envify/custom');
var watchify = require('watchify');
var babelify = require('babelify');
var source = require('vinyl-source-stream'),
    sourceFile = './js/index.js',
    destFolder = './dist/scripts',
    destFileName = 'bundle.js';

var bundler = watchify(
    browserify({
    entries: [sourceFile],
    debug: true,
    insertGlobals: true,
    cache: {},
    packageCache: {},
    fullPaths: true
}))
    .transform(babelify)
    .transform(envify({ NODE_ENV: 'development' }));

bundler.on('update', rebundle);
bundler.on('log', $.util.log);

function rebundle() {
    return bundler.bundle()
        // log errors if they happen
        .on('error', $.util.log.bind($.util, 'Browserify Error'))
        .pipe(source(destFileName))
        .pipe(gulp.dest(destFolder));
}

// Styles
gulp.task('styles', ['less']);

gulp.task('less', function() {
    return gulp.src(['less/**/*.less', 'less/**/*.css'])
        .pipe($.less({
            precision: 10,
            paths: [path.join(__dirname, 'app', 'styles')]
        }))
        .pipe(gulp.dest('dist/styles'));
});

// Scripts
gulp.task('scripts', rebundle);

gulp.task('buildScripts', function() {
    return browserify({
        entries: [sourceFile],
        insertGlobals: true,
        fullPaths: true
    })
        .transform(babelify)
        .transform(envify({ NODE_ENV: 'production' }))
        .bundle()
        .pipe(source(destFileName))
        .pipe(gulp.dest('dist/scripts'));
});

// Build/deploy scripts
gulp.task('deploymentScripts', function() {
    return gulp.src('build/*')
        .pipe($.useref())
        .pipe(gulp.dest('dist/build'))
        .pipe($.size());
});

// Clean
gulp.task('clean', function(cb) {
    $.cache.clearAll();
    cb(del.sync(['dist/scripts']));
});

// Bundle
gulp.task('bundle', ['styles', 'scripts', 'bower']);

gulp.task('buildBundle', ['styles', 'buildScripts', 'bower']);

// Bower helper
gulp.task('bower', function() {
    gulp.src('bower_components/**/*', {
        base: 'bower_components'
    })
        .pipe(gulp.dest('dist/bower_components/'));
});

// Watch
gulp.task('watch', ['bundle'], function () {
    gulp.watch(['less/**/*.less', 'less/**/*.css'], ['styles']);
});

// Build
gulp.task('build', ['buildBundle', 'deploymentScripts'], function() {
    gulp.src('bundle.js')
        .pipe($.uglify())
        .pipe($.stripDebug())
        .pipe(gulp.dest('dist/scripts'));
});

// Default task
gulp.task('default', ['clean', 'build']);
