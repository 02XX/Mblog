// 函数的含义是，在第index个标题处生成目录树，该标题级别为hLevel
function genFromTitle(hLevel, index) {
    let ele = ''
    while (index < $('.isTitle').length) {
        let t = $('.isTitle').eq(index)
        if (t.attr('hLevel') > hLevel) {
            // 遇到更小的标题，递归生成
            let nt = genFromTitle(t.attr('hLevel'), index)
            ele += `<li>${nt.ele}</li>`
            // 从nt.index到index-1的标题都处理完毕，更新index
            index = nt.index
        }
        else if (t.attr('hLevel') < hLevel) break // 遇到更大的标题，向上返回
        else {
            // 相同等级平行关系，直接添加标题项，下一个
            ele += `<li>
						<a> ${t.text()} </a>
					</li>`;
            index++;
        }
    }
    ele = `<ul>${ele}</ul>`
    return { ele, index } //index 也要返回去，父函数继续往后生成
}

// elEssay为文档挂载点，elContent为生成的目录挂载点
function makeEssayContent(elEssay, elContent) {
    // 首先标记所有标题
    for (let i = 1; i <= 6; i++) {
        elEssay.find('h' + i).addClass('isTitle').attr('hLevel', i)
    }
    elContent.html(genFromTitle(1, 0).ele);//从第一个一级标题开始生成
}