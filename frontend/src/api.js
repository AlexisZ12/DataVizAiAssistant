async function post(path, body) {
  const res = await fetch(path, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  })
  if (!res.ok) {
    let msg = `请求失败（${res.status}）`
    try {
      const j = await res.json()
      if (j.detail) msg = j.detail
    } catch {
      /* 非 JSON 响应，保留默认提示 */
    }
    throw new Error(msg)
  }
  return res.json()
}

export const generateChart = (payload) => post('/api/charts/generate', payload)
export const modifyData = (payload) => post('/api/charts/modify-data', payload)
export const modifyStyle = (payload) => post('/api/charts/modify-style', payload)
