/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let inti = init;
    return {
        increment: function(){
            return ++inti
        },
        decrement: function() {
            return --inti
        },
        reset: function() {
            inti = init
            return inti
        }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */