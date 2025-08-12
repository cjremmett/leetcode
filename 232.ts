class MyQueue {
    s: Array<number> = [];

    constructor() {
    }

    push(x: number): void {
        console.log(`Pushing ${x}`);
        let st: Array<number> = [];
        let numOps = this.s.length;
        for(let i = 0; i < numOps; i++)
        {
            let tempNum = this.s.pop();
            if(typeof tempNum === 'number')
            {
                st.push(tempNum);
            }
        }

        this.s.push(x);

        for(let j = 0; j < numOps; j++)
        {
            let tempNum = st.pop();
            if(typeof tempNum === 'number')
            {
                this.s.push(tempNum);
            }
        }

        console.log(`After pushing ${x}, s is ${this.s}`);
    }

    pop(): number | undefined {
        if(this.s.length > 0)
        {
            return this.s.splice(-1)[0];
        }
        else
        {
            return undefined;
        }
    }

    peek(): number | undefined {
        if(this.s.length > 0)
        {
            return this.s[this.s.length - 1];
        }
        else
        {
            return undefined;
        }
    }

    empty(): boolean {
        return (this.s.length == 0) ? true : false;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */