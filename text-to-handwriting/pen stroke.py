<canvas id="canvas"></canvas>
<script>
  const canvas = document.getElementById('canvas');
  const ctx = canvas.getContext('2d');
  let isDrawing = false;
  let currentLine = [];
  const lineWidthMin = 1;
  const lineWidthMax = 5;

  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;

  canvas.addEventListener('mousedown', startDrawing);
  canvas.addEventListener('mousemove', draw);
  canvas.addEventListener('mouseup', endDrawing);

  function startDrawing(e) {
    isDrawing = true;
    currentLine = [{ x: e.clientX, y: e.clientY }];
  }

  function draw(e) {
    if (!isDrawing) return;

    const lastPoint = currentLine[currentLine.length - 1];
    const newPoint = { x: e.clientX, y: e.clientY };
    if (distance(lastPoint, newPoint) > 2) { // Only add points if they are far enough
      currentLine.push(newPoint);
      drawLineSegment(lastPoint, newPoint);
    }
  }

  function endDrawing(e) {
    if (!isDrawing) return;
    isDrawing = false;

    currentLine.push({ x: e.clientX, y: e.clientY });
    drawLineSegment(currentLine[currentLine.length - 2], currentLine[currentLine.length - 1]);
    smoothStroke();
  }

  // Draw a segment between two points
  function drawLineSegment(point1, point2) {
    ctx.beginPath();
    ctx.moveTo(point1.x, point1.y);
    ctx.lineTo(point2.x, point2.y);
    ctx.strokeStyle = '#000';
    ctx.lineWidth = lineWidthMax;
    ctx.stroke();
  }

  // Smooth out the stroke by gradually reducing line width at the end
  function smoothStroke() {
    const last6Points = currentLine.slice(-6);
    last6Points.forEach((point, index) => {
      if (index > 0) {
        const prevPoint = last6Points[index - 1];
        ctx.beginPath();
        ctx.moveTo(prevPoint.x, prevPoint.y);
        ctx.lineTo(point.x, point.y);
        ctx.lineWidth = lineWidthMax - (index * (lineWidthMax - lineWidthMin) / 6);
        ctx.stroke();
      }
    });
  }

  // Utility to calculate the distance between two points
  function distance(point1, point2) {
    return Math.sqrt(Math.pow(point2.x - point1.x, 2) + Math.pow(point2.y - point1.y, 2));
  }
</script>
