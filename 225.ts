class MyStack {

    q: Array<number>

    constructor() {
        this.q = [];
    }

    push(x: number): void {
        this.q.push(x);
        for(let i = 0; i < this.q.length - 1; i++) 
        {
            let num = this.q.shift();
            if (num !== undefined) 
            {
                this.q.push(num);
            }
        }
    }

    pop(): (number | undefined) {
        if(this.q.length > 0)
        {
            return this.q.shift();
        }
        else
        {
            return undefined;
        }
    }

    top(): (number | undefined) {
        if(this.q.length > 0)
        {
            return this.q[0];
        }
        else
        {
            return undefined;
        }
    }

    empty(): boolean {
        return this.q.length === 0;
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * var obj = new MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */