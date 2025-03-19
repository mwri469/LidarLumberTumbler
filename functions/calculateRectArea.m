function area = calculateRectArea(length, widthDist)
  % Function to calculate the area of a rectangle from length and width
  % Written to test functionality of the `arguments' block in Octave
  % By:   Martin Wright
  % Date: 13 MAR 2025
  arguments
    length {mustBePositive}
    widthDist {mustBePositive} = 15
  end

  area = widthDist * length;
end
