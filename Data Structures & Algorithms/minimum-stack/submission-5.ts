class MinStack {
    stack:  Array<number>;
    min_stack:  Array<number>;
    
    constructor() {
        this.stack = new Array<number>();
        this.min_stack = new Array<number>();
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val: number): void {
        const currentMin = this.min_stack.length
            ? this.min_stack[this.min_stack.length - 1]
            : val;
        this.min_stack.push(Math.min(val, currentMin));
        this.stack.push(val);
    }

    /**
     * @return {void}
     */
    pop(): void {
        if (this.stack.length != 0){
            this.min_stack.pop();
            this.stack.pop();
        }
    }

    /**
     * @return {number}
     */
    top(): number {
        if (this.stack.length != 0){
            return this.stack[this.min_stack.length - 1];
        }
        return -1;
    }

    /**
     * @return {number}
     */
    getMin(): number {
        if (this.stack.length != 0){
            return this.min_stack[this.min_stack.length - 1];
        }
        return -1;
    }
}
