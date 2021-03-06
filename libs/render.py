from rest_framework.renderers import JSONRenderer

class CustomRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        结构
        {
            'code':xxx,
            'msg':请求成功,
            'data':{返回数据}
        }
        """
        if renderer_context:
            if isinstance(data, dict):
            #如果没有就创建一个
                msg = data.pop('msg', '请求成功')
                code = data.pop('code', 0)
            else:
                msg = '请求成功'
                code = 0
            response = renderer_context['response']
            response.status_code = 200
            res = {
                'code': code,
                'msg': msg,
                'data': data
            }
            return super().render(res, accepted_media_type, renderer_context)
        else:
            return super().render(data, accepted_media_type, renderer_context)