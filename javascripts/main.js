function getTemplateAjax(path, callback) {
    var source, template;
    $.ajax({
        url: path,
        success: function (data) {
            source = data;
            template = Handlebars.compile(source);
            if (callback) callback(template);
        }
    });
}

function rndTpl(tpl, els, data) {
    getTemplateAjax(tpl, function(template) {
        $(els).html(template(data));
    });
}

function renderPortlet(jsonsrc, tpl, el) {
    $.getJSON(jsonsrc, function (data) {
        rndTpl(tpl, el, data);
    });
}

/* Thanks! http://doginthehat.com.au/2012/02/comparison-block-helper-for-handlebars-templates/#comment-44 */
Handlebars.registerHelper('compare', function (lvalue, operator, rvalue, options) {

    var operators, result;
    if (arguments.length < 3) {
        throw new Error("Handlerbars Helper 'compare' needs 2 parameters");
    }
    
    if (options === undefined) {
        options = rvalue;
        rvalue = operator;
        operator = "===";
    }

    operators = {
        '==': function (l, r) { return l == r; },
        '===': function (l, r) { return l === r; },
        '!=': function (l, r) { return l != r; },
        '!==': function (l, r) { return l !== r; },
        '<': function (l, r) { return l < r; },
        '>': function (l, r) { return l > r; },
        '<=': function (l, r) { return l <= r; },
        '>=': function (l, r) { return l >= r; },
        'typeof': function (l, r) { return typeof l == r; }
    };
    
    if (!operators[operator]) {
        throw new Error("Handlerbars Helper 'compare' doesn't know the operator " + operator);
    }
    
    result = operators[operator](lvalue, rvalue);
    
    if (result) {
        return options.fn(this);
    } else {
        return options.inverse(this);
    }
});
