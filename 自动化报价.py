from flask import Flask, request, render_template_string

app = Flask(__name__)

# Data dictionaries
categories = {'旋回破衬板': 1.3, '圆锥破衬板': 1.15, '鄂板': 1.0, '锤头': 1.0}
materials = {'Mn18Cr2': 12100, 'Mn13Cr2': 11300, 'Cr26': 19000, 'Cr20': 18000}
profit_margins = {'高': 0.30, '中': 0.20, '低': 0.10}

# Function to calculate prices
def calculate_price(product_type, material, weight, quantity, margin_level):
    category_coefficient = categories[product_type]
    material_cost = materials[material]
    margin = profit_margins[margin_level]
    # Updated calculation to include weight
    unit_price = (material_cost / (1 - (category_coefficient * margin))) * weight
    total_price = unit_price * quantity
    tax_price = total_price * 0.13
    return unit_price, total_price, tax_price

# Route to handle the form
@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        product_type = request.form.get('product_type')
        material = request.form.get('material')
        weight = float(request.form.get('weight'))  # Get weight input as float
        quantity = int(request.form.get('quantity'))
        margin_level = request.form.get('margin_level')
        unit_price, total_price, tax_price = calculate_price(product_type, material, weight, quantity, margin_level)
        result = f"单价: {unit_price:.2f}, 总价: {total_price:.2f}, 含税金: {tax_price:.2f}"
        return result
    return '''
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
            <br>
            期望说明：<br>
            高 - 例如客户原来使用美卓原厂件，或者对方价格不敏感，质量要求高。<br>
            中 - 期望收益的高和低是比较明确的，其他情况可以在中值附近考虑。<br>
            低 - 例如客户是代理商或者对三方耐磨件很熟悉。<br>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
