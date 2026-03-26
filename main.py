import json
import time
import random
from datetime import datetime
from typing import Dict, List, Optional

class AIMaterialGenerator:
    """AI广告素材生成器模拟类"""
    
    def __init__(self):
        self.history_data = []
        self.templates = [
            "夏季清凉穿搭，{product}让你时尚又舒适",
            "限时特惠！{product}直降{percent}%",
            "网红同款{product}，点击立即购买",
            "{product}新品上市，前{count}名送好礼"
        ]
        
    def analyze_history_data(self, product_type: str) -> Dict:
        """分析历史投放数据（模拟）"""
        print(f"正在分析{product_type}类目的历史投放数据...")
        time.sleep(0.5)
        
        # 模拟分析结果
        analysis_result = {
            "best_performing_time": "19:00-22:00",
            "top_keywords": ["时尚", "舒适", "优惠", "新品"],
            "avg_ctr": 0.025,  # 平均点击率2.5%
            "recommended_templates": [0, 2]  # 推荐使用的模板索引
        }
        return analysis_result
    
    def generate_text_material(self, product: str, template_idx: int) -> str:
        """生成文本素材（模拟GPT-4文本生成）"""
        template = self.templates[template_idx]
        
        # 模拟GPT-4的变量填充
        if "{percent}" in template:
            percent = random.randint(20, 50)
            material = template.replace("{product}", product).replace("{percent}", str(percent))
        elif "{count}" in template:
            count = random.randint(100, 500)
            material = template.replace("{product}", product).replace("{count}", str(count))
        else:
            material = template.replace("{product}", product)
            
        print(f"文本素材生成完成: {material}")
        return material
    
    def generate_video_prompt(self, text_material: str) -> str:
        """生成视频生成提示词（模拟Stable Diffusion提示词生成）"""
        print("正在生成视频制作提示词...")
        time.sleep(0.3)
        
        # 基于文本素材生成视频提示词
        video_prompts = [
            f"高清广告视频，{text_material}，专业摄影，明亮背景",
            f"短视频广告，{text_material}，模特展示，动态转场",
            f"产品特写视频，{text_material}，慢动作，电影质感"
        ]
        
        return random.choice(video_prompts)
    
    def estimate_ctr(self, material: str, product_type: str) -> float:
        """预估点击率（模拟AI预测）"""
        # 简单的关键词匹配来模拟CTR预测
        boost_keywords = ["限时", "特惠", "直降", "送好礼", "新品"]
        base_ctr = 0.025
        
        boost = 0
        for keyword in boost_keywords:
            if keyword in material:
                boost += 0.005
                
        # 服装类目额外加成
        if "服装" in product_type or "穿搭" in product_type:
            boost += 0.003
            
        estimated_ctr = base_ctr + boost
        return round(estimated_ctr, 4)
    
    def batch_generate(self, product: str, product_type: str, count: int) -> List[Dict]:
        """批量生成素材"""
        print(f"开始为{product}批量生成{count}条素材...")
        
        analysis = self.analyze_history_data(product_type)
        materials = []
        
        for i in range(count):
            # 使用推荐模板或随机选择
            if i < len(analysis["recommended_templates"]):
                template_idx = analysis["recommended_templates"][i]
            else:
                template_idx = random.randint(0, len(self.templates)-1)
            
            # 生成素材
            text_material = self.generate_text_material(product, template_idx)
            video_prompt = self.generate_video_prompt(text_material)
            estimated_ctr = self.estimate_ctr(text_material, product_type)
            
            material_data = {
                "id": i + 1,
                "product": product,
                "text_material": text_material,
                "video_prompt": video_prompt,
                "estimated_ctr": estimated_ctr,
                "generated_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "template_used": template_idx
            }
            
            materials.append(material_data)
            self.history_data.append(material_data)
            
            # 模拟生成间隔
            time.sleep(0.2)
            
        return materials
    
    def generate_report(self, materials: List[Dict]) -> Dict:
        """生成生成报告"""
        total_count = len(materials)
        avg_ctr = sum(m["estimated_ctr"] for m in materials) / total_count
        best_material = max(materials, key=lambda x: x["estimated_ctr"])
        
        report = {
            "total_generated": total_count,
            "average_ctr": round(avg_ctr, 4),
            "best_material_id": best_material["id"],
            "best_material_text": best_material["text_material"],
            "best_estimated_ctr": best_material["estimated_ctr"],
            "generation_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "time_saved": "约3.5小时/条"  # 模拟从4小时缩短到30分钟
        }
        
        return report

def main():
    """主函数"""
    print("=" * 50)
    print("AI智能广告素材生成系统")
    print("=" * 50)
    
    # 初始化生成器
    generator = AIMaterialGenerator()
    
    # 模拟服装类目广告素材生成
    product_name = "时尚T恤"
    product_type = "服装类目"
    
    print(f"\n产品: {product_name}")
    print(f"类目: {product_type}")
    
    # 批量生成5条测试素材
    batch_size = 5
    materials = generator.batch_generate(product_name, product_type, batch_size)
    
    # 生成报告
    report = generator.generate_report(materials)
    
    print("\n" + "=" * 50)
    print("生成报告:")
    print("=" * 50)
    print(f"总生成数量: {report['total_generated']}条")
    print(f"平均预估点击率: {report['average_ctr']*100:.2f}%")
    print(f"最佳素材(ID:{report['best_material_id']}): {report['best_material_text']}")
    print(f"最佳素材预估点击率: {report['best_estimated_ctr']*100:.2f}%")
    print(f"单条素材制作时间节省: {report['time_saved']}")
    print(f"报告生成时间: {report['generation_time']}")
    
    # 模拟效果提升
    original_ctr = 0.025
    improved_ctr = report['average_ctr']
    improvement = (improved_ctr - original_ctr) / original_ctr * 100
    
    print(f"\n预估点击率提升: {improvement:.1f}%")
    print("=" * 50)
    print("素材生成完成！")

if __name__ == "__main__":
    main()