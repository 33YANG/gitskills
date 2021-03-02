const fs = require('fs').promises
const path = require('path')

const ignoreFolder = ['node_modules', '.vscode']

/**
 * Get and count each file extname
 * @param {string} dir The directory
 * @return {object} The result object
 */
async function getFileExt(dir) {
  let countFileExt = {}
  let curDir = await fs.readdir(path.resolve(dir)) || []
  curDir = curDir.filter(item => {
    return !ignoreFolder.includes(item)
  })
  for (const item of curDir) {
    const curPath = path.resolve(dir, item)
    const isFile = (await fs.stat(curPath)).isFile()
    if (isFile) {
      const extName = path.extname(curPath) ? path.extname(curPath) : '_noExt'
      countFileExt[extName] ? countFileExt[extName]++ : countFileExt[extName] = 1
    } else {
      countFileExt = mergeObj(countFileExt, await getFileExt(curPath))
    }
  }
  return countFileExt
}

/**
 * Merge two object use keys
 * @param {object} concatObj The concat object
 * @param {object} targetObj The target object
 * @return {object} Result
 */
function mergeObj(concatObj, targetObj) {
  let obj = concatObj
  Object.keys(targetObj).forEach(key => {
    obj[key] = concatObj[key] ? obj[key] + targetObj[key] : targetObj[key]
  })
  return obj
}

try {
  ;(async function() {
    console.log('Waiting...')
    console.log(JSON.stringify(await getFileExt('./'), null, 2))
  })()
} catch (error) {
  console.error('Catch Error:', error)
}
