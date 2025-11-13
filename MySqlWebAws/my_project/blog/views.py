from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.shortcuts import render
from .models import Post  # Import model Post của bạn
from .forms import PostForm

# Hàm này sẽ được gọi bởi URL
def post_list(request):
    # 1. Lấy tất cả đối tượng Post từ CSDL, sắp xếp theo ngày tạo mới nhất
    posts = Post.objects.all().order_by('-created_at')

    # 2. Gửi dữ liệu 'posts' đến một file template
    # (Chúng ta sẽ tạo file 'blog/post_list.html' ở bước tiếp theo)
    context = {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    # Lấy đối tượng Post có 'pk' (primary key) bằng với pk từ URL
    # Nếu không tìm thấy, nó sẽ tự động trả về lỗi 404
    post = get_object_or_404(Post, pk=pk)

    context = {
        'post': post,
    }
    # Render một file template mới tên là 'post_detail.html'
    return render(request, 'blog/post_detail.html', context)

# Trong file blog/views.py

# Thêm 'redirect' vào dòng import 'render'
def post_create(request):
    if request.method == "POST":
        # Nếu là gửi dữ liệu (POST)
        form = PostForm(request.POST)
        if form.is_valid():
            # Nếu dữ liệu hợp lệ, lưu vào CSDL
            post = form.save()
            # Chuyển hướng đến trang chi tiết của bài vừa tạo
            return redirect('post_detail', pk=post.pk)
    else:
        # Nếu là xem trang (GET)
        # Hiển thị một form rỗng
        form = PostForm()

    # Gửi 'form' đến template
    return render(request, 'blog/post_form.html', {'form': form})

# Trong file blog/views.py
# ... (các import và các view khác của bạn) ...

# Thêm hàm mới này:
def post_update(request, pk):
    # 1. Lấy bài đăng cũ từ CSDL
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        # 2. Khi gửi: Truyền 'instance=post'
        #    để form biết đây là CẬP NHẬT, không phải TẠO MỚI
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        # 3. Khi xem: Truyền 'instance=post'
        #    để form hiển thị dữ liệu cũ của bài đăng này
        form = PostForm(instance=post)

    # 4. Tái sử dụng cùng một template!
    return render(request, 'blog/post_form.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')

    return render(request, 'blog/post_confirm_delete.html', {'post': post})