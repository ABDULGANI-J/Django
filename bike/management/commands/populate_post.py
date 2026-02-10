from bike.models import Post,Category
from django.core.management import BaseCommand
import random


class Command(BaseCommand):
    help = "This Command inserts post data"

    def handle(self, *args, **options):
            Post.objects.all().delete()

            titles = [
            "Ride the Future with Smart Bike Booking",
            "Power Meets Performance",
            "Explore the City on Two Wheels",
            "Designed for Riders Who Love Speed",
            "Smooth Rides, Strong Engines",
            "Book Your Dream Bike Instantly",
            "Where Style Meets Mileage",
            "Built for Roads, Built for You",
            "Experience Freedom on Every Ride",
            "Bikes That Match Your Lifestyle",
            "Adventure Starts with the Right Bike",
            "Fast, Furious, and Fuel Efficient",
            "Your Daily Ride, Redefined",
            "Engineered for Indian Roads",
            "Ride Smart, Ride Safe",
            "The Perfect Bike for Every Journey",
            "Performance You Can Trust",
            "Turn Every Road into an Adventure",
            "Built to Rule the Streets",
            "Ride More, Wait Less"
            ]

            contents = [
            "Discover a seamless bike booking experience with powerful performance and modern design.",
            "Our bikes deliver unmatched engine strength and smooth handling for city and highway rides.",
            "Navigate through traffic effortlessly with our lightweight and fuel-efficient bikes.",
            "Crafted for riders who value speed, control, and comfort in every ride.",
            "Enjoy superior mileage and long-lasting performance built for daily use.",
            "Choose your favorite bike online and get ready to ride in just a few clicks.",
            "Stylish bikes that balance premium looks with excellent fuel efficiency.",
            "Engineered to handle tough road conditions with ease and comfort.",
            "Feel the joy of smooth and stress-free riding wherever you go.",
            "Find the perfect bike that fits your daily commute and weekend rides.",
            "Adventure-ready bikes designed for long rides and rough terrains.",
            "High performance engines combined with impressive mileage.",
            "Redefining everyday commuting with comfort-focused bike design.",
            "Tested and trusted bikes built specially for Indian road conditions.",
            "Advanced braking and safety features for confident riding.",
            "From short city rides to long trips, there’s a bike for every need.",
            "Built with high-quality materials to deliver reliable performance.",
            "Make every ride exciting with premium bikes and smooth handling.",
            "Street-dominating design with powerful performance and style.",
            "Instant bike booking so you can spend more time riding."
            ]

            img_urls = [
                "https://images.unsplash.com/photo-1518655048521-f130df041f66?w=700&h=800&fit=crop",
                "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=700&h=800&fit=crop",
                "https://images.unsplash.com/photo-1558981806-ec527fa84c39?w=700&h=800&fit=crop",
                "https://images.unsplash.com/photo-1524041255072-7da0525d6b34?w=700&h=800&fit=crop",
                "https://images.unsplash.com/photo-1563720223185-11003d516935?w=700&h=800&fit=crop",
                "https://images.unsplash.com/photo-1542362567-b07e54358753?w=700&h=800&fit=crop",
                "https://images.unsplash.com/photo-1511919884226-fd3cad34687c?w=700&h=800&fit=crop",
                "https://images.unsplash.com/photo-1493238792000-8113da705763?w=700&h=800&fit=crop",
                "https://images.unsplash.com/photo-1502877338535-766e1452684a?w=700&h=800&fit=crop",
                "https://images.unsplash.com/photo-1589187775328-36c2c2c63b9c?w=700&h=800&fit=crop",
                "https://images.unsplash.com/photo-1558980664-10eb0c1c21c7?w=700&h=800&fit=crop",
                "https://images.unsplash.com/photo-1558981033-06e3d45f4b49?w=700&h=800&fit=crop",
                "https://images.unsplash.com/photo-1558981285-6f0c94958bb6?w=700&h=800&fit=crop",
                "https://images.unsplash.com/photo-1558981403-c5f9891d65c4?w=700&h=800&fit=crop",
                "https://images.unsplash.com/photo-1549298916-b41d501d3772?w=700&h=800&fit=crop",
                "https://images.unsplash.com/photo-1568772585407-9361f9bf3a87?w=700&h=800&fit=crop",
                "https://images.unsplash.com/photo-1532298229144-0ec0c57515c7?w=700&h=800&fit=crop",
                "https://images.unsplash.com/photo-1549921296-3fd62d0d4c9d?w=700&h=800&fit=crop",
                "https://images.unsplash.com/photo-1519681393784-d120267933ba?w=700&h=800&fit=crop",
                "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=700&h=800&fit=crop",
            ]

            categories = Category.objects.all()
            for title, content, img_url in zip(titles, contents, img_urls):
                category = random.choice(categories)
                Post.objects.create(title=title, content=content, img_url=img_url, category=category)

            self.stdout.write(self.style.SUCCESS("commpleted inserting data!"))