# Data dictionaries
categories = {'旋回破衬板': 1.3, '圆锥破衬板': 1.15, '鄂板': 1.0, '锤头': 1.0}
materials = {'Mn18Cr2': 12100, 'Mn13Cr2': 11300, 'Cr26': 19000, 'Cr20': 18000}
profit_margins = {'高': 0.30, '中': 0.20, '低': 0.10}

def calculate_price(product_type, material, weight, quantity, margin_level):
    """
    计算基于产品类型、材料、重量、数量和利润等级的价格。

    参数:
    product_type (str): 产品类型。
    material (str): 材料类型。
    weight (float): 产品重量，单位吨。
    quantity (int): 产品数量。
    margin_level (str): 利润等级。

    返回:
    tuple: 返回包含单位价格、总价格和含税价格的元组。
    """
    if product_type not in categories:
        raise ValueError(f"未知的产品类型: {product_type}")
    if material not in materials:
        raise ValueError(f"未知的材料类型: {material}")
    if margin_level not in profit_margins:
        raise ValueError(f"未知的利润等级: {margin_level}")

    category_coefficient = categories[product_type]
    material_cost = materials[material]
    margin = profit_margins[margin_level]
    unit_price = (material_cost / (1 - (category_coefficient * margin))) * weight
    total_price = unit_price * quantity
    tax_price = total_price * 0.13
    return unit_price, total_price, tax_price
