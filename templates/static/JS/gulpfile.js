const gulp = require('gulp');
// const uglify = require('gulp-uglify');
// const rename = require("gulp-rename");
// const pipeline = require('readable-stream').pipeline;
// const uglify = require('gulp-uglify-es').default;
const cleanCSS = require('gulp-clean-css');
// const htmlmin = require('gulp-htmlmin');
// const minifyInline = require('gulp-minify-inline');

/*function uglifying() {

    return gulp.src('public/js/!*.js')
    // .pipe(rename("timing.js"))
        .pipe(uglify(/!* options *!/))
        .pipe(gulp.dest('public/dist/js/'));

}*/


function minifyingCss() {

    return gulp.src('templates/static/css/*.css')
        .pipe(cleanCSS({compatibility: 'ie8'}))
        .pipe(gulp.dest('templates/static/css/'));
}


/*function minifyingHtml() {

    return gulp.src('views/!*')
        .pipe(htmlmin({
            collapseWhitespace: true,
            removeComments: true,
            removeOptionalTags: true,
        }))
        .pipe(gulp.dest('./views/dist'));

}*/


/*function minifyingInline() {
    return gulp.src('views/dist/!*')
        .pipe(minifyInline())
        .pipe(gulp.dest('views/dist'))

}*/

/*function uglifyingApp() {

    return gulp.src('app.js')
    // .pipe(rename("timing.js"))
        .pipe(uglify(/!* options *!/))
        .pipe(gulp.dest('dist'));

}*/


gulp.task('default', gulp.series(minifyingCss));