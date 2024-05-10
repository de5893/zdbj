from flask import request, render_template_string
from wxcloudrun.model import calculate_price  # 确保model.py中有calculate_price函数的定义

def init_app(app):
    @app.route('/', methods=['GET', 'POST'])
    def form():
        if request.method == 'POST':
            product_type = request.form.get('product_type')
            material = request.form.get('material')
            weight = float(request.form.get('weight'))  # 获取重量输入并转换为浮点数
            quantity = int(request.form.get('quantity'))  # 获取数量输入并转换为整数
            margin_level = request.form.get('margin_level')
            unit_price, total_price, tax_price = calculate_price(product_type, material, weight, quantity, margin_level)
            result = f"单价: {unit_price:.2f}元, 总价: {total_price:.2f}元, 含税金: {tax_price:.2f}元"
            return result
        return render_template_string('''
            <html>
            <body>
                <style>
                input, select {
                    width: 300px;
                    height: 35px;
                    margin: 5px 0;
                }
                </style>
                <form method="post">
                    类别: <select name="product_type">
                        <option value="旋回破衬板">旋回破衬板</option>
                        <option value="圆锥破衬板">圆锥破衬板</option>
                        <option value="鄂板">鄂板</option>
                        <option value="锤头">锤头</option>
                    </select><br>
                    材质: <select name="material">
                        <option value="Mn18Cr2">Mn18Cr2</option>
                        <option value="Mn13Cr2">Mn13Cr2</option>
                        <option value="Cr26">Cr26</option>
                        <option value="Cr20">Cr20</option>
                    </select><br>
                    重量: <input type="number" name="weight" min="0.001" step="0.001" required>(吨)<br>
                    数量: <input type="number" name="quantity" min="1" max="10000" required><br>
                    期望收益: <select name="margin_level">
                        <option value="高">高 - 高收益</option>
                        <option value="中">中 - 适用于大多数情况</option>
                        <option value="低">低 - 底线价格</option>
                    </select><br>
                    <input type="submit" value="计算价格"><br>
                </form>
            </body>
            </html>
        ''')
