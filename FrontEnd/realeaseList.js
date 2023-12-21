export class RealeaseList{
    constructor(fonte){
        this.source = fonte
        this.__schedule = null
    }

    
    async __getList() {
        let releaseList = []
        releaseList = await fetch('../weekAnimeDays.json')
            .then(response => response.json())
            .then((animelist)=>{
                // console.log(animelist)
                return animelist
            });
        return releaseList
    }

    async initList () {
        this.__schedule = await this.__getList()
    }
}

